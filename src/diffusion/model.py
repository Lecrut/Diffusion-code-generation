import torch
import torch.nn as nn
import torch.nn.functional as F
import math

# TODO: przemyśleć, sprawdzić, napisać trening
class SinusoidalPositionEmbeddings(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim

    def forward(self, time):
        half_dim = self.dim // 2
        embeddings = math.log(10000) / (half_dim - 1)
        embeddings = torch.exp(torch.arange(half_dim, device=time.device) * -embeddings)
        embeddings = time[:, None] * embeddings[None, :]
        embeddings = torch.cat((embeddings.sin(), embeddings.cos()), dim=-1)
        return embeddings

class AutoDiffuCoder(nn.Module):
    def __init__(
            self, 
            vocab_size,
            mask_token_id, 
            hidden_dim=512, 
            num_layers=8, 
            num_heads=8, 
            context_dim=768, 
            max_seq_len=1000, 
            inference_steps=500
            ):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.vocab_size = vocab_size
        self.mask_token_id = mask_token_id
        self.max_seq_len = max_seq_len
        self.inference_steps = inference_steps # Np. 500 iteracji przy generowaniu
        
        self.token_embedding = nn.Embedding(vocab_size, hidden_dim)
        self.positional_encoding = nn.Parameter(torch.randn(1, max_seq_len, hidden_dim))
        
        self.time_mlp = nn.Sequential(
            SinusoidalPositionEmbeddings(hidden_dim),
            nn.Linear(hidden_dim, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        
        self.context_proj = nn.Linear(context_dim, hidden_dim)
        
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=hidden_dim, 
            nhead=num_heads, 
            dim_feedforward=hidden_dim * 4,
            batch_first=True, 
            norm_first=True, 
            activation="gelu"
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.lm_head = nn.Linear(hidden_dim, vocab_size)

    def _step_forward(self, masked_input_ids, t, context_embedding):
        """Wewnętrzna metoda - jedno przejście przez sieć (używane w treningu i w pętli)"""
        _, seq_len = masked_input_ids.shape
        
        x = self.token_embedding(masked_input_ids) + self.positional_encoding[:, :seq_len, :]
        t_emb = self.time_mlp(t).unsqueeze(1)
        x = x + t_emb
        
        ctx_emb = self.context_proj(context_embedding)
        transformer_in = torch.cat([ctx_emb, x], dim=1)
        out = self.transformer(transformer_in)
        
        code_out = out[:, ctx_emb.size(1):, :]
        return self.lm_head(code_out)

    @torch.no_grad()
    def _generate_loop(self, context_embedding):
        """Magiczna pętla, która robi wszystko za Ciebie"""
        batch_size = context_embedding.size(0)
        device = context_embedding.device
        
        # 1. Startujemy z tablicą w 100% wypełnioną [MASK]
        current_ids = torch.full((batch_size, self.max_seq_len), self.mask_token_id, device=device)
        
        for step in range(self.inference_steps):
            # Czas biegnie od inference_steps w dół do 0
            current_t_val = self.inference_steps - step
            t = torch.full((batch_size,), current_t_val, device=device)
            
            # 2. Model zgaduje co jest pod maskami
            logits = self._step_forward(current_ids, t, context_embedding)
            
            # Obliczamy prawdopodobieństwa (softmax) i wybieramy najbardziej prawdopodobne tokeny
            probs = F.softmax(logits, dim=-1)
            confidence, predicted_ids = torch.max(probs, dim=-1)
            
            # 3. Jeśli token NIE BYŁ maską, nie ruszamy go (już go wcześniej odsłoniliśmy i ufamy mu)
            is_mask = (current_ids == self.mask_token_id)
            
            # Ignorujemy pewność dla tokenów, które już są odsłonięte, żeby ich nie zepsuć
            confidence[~is_mask] = float('inf') 
            
            # 4. Harmonogram masek: ile masek ma ZOSTAĆ w tym kroku?
            # Spada liniowo np. od 1000 masek do 0 na końcu
            ratio = (self.inference_steps - step - 1) / self.inference_steps
            num_masks_to_keep = int(ratio * self.max_seq_len)
            
            if num_masks_to_keep > 0:
                # Szukamy tokenów z NAJMNIEJSZĄ pewnością, by ponownie je zamaskować
                # (czyli te, co do których model był pewny, zostają trwale odsłonięte)
                mask_threshold = torch.topk(confidence, k=num_masks_to_keep, dim=-1, largest=False).values[:, -1:]
                tokens_to_mask = confidence <= mask_threshold
                
                # Zapisujemy wytypowane tokeny, ale wymuszamy maski tam, gdzie pewność była najsłabsza
                current_ids = predicted_ids
                current_ids[tokens_to_mask] = self.mask_token_id
            else:
                # Ostatni krok - zdejmujemy wszystko
                current_ids = predicted_ids
                
        return current_ids

    def forward(self, context_embedding, masked_input_ids=None, t=None):
        """
        Główny interfejs modelu. Decyduje, co zrobić na podstawie przekazanych argumentów.
        """
        # Jeśli jesteśmy w trybie treningowym i podaliśmy dane do nauki:
        if self.training and masked_input_ids is not None and t is not None:
            return self._step_forward(masked_input_ids, t, context_embedding)
        
        # W przeciwnym razie - pełen automat do generowania:
        self.eval() # Zabezpieczenie, upewniamy się że nie psujemy wag
        return self._generate_loop(context_embedding)
    

# Słownik np. 10 000 słów, token maski to 9999
# Definiujesz parametry o które prosiłeś: np. 1000 tokenów sekwencji w 500 iteracjach.
# model = AutoDiffuCoder(
#     vocab_size=10000, 
#     mask_token_id=9999, 
#     max_seq_len=1000, 
#     inference_steps=500
# )

# # --- GDY TRENUJESZ ---
# model.train()
# # (Wewnątrz pętli treningowej podajesz zaszumione dane i czas)
# logits = model(prompt_embedding, zaszumiony_kod, kroki_t)
# # loss = compute_loss(logits, ...)


# # --- GDY GENERUJESZ (Czysta Magia) ---
# model.eval()
# # Po prostu wrzucasz swoje polecenie tekstowe (już zakodowane jako tensor)!
# gotowy_kod_ids = model(prompt_embedding)

# Na koniec tylko dekodujesz otrzymaną tablicę liczb z powrotem na tekst
# print(tokenizer.decode(gotowy_kod_ids))