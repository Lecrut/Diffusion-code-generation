import os
import shutil
import pandas as pd

# 1. Definicja ścieżek
base_dir = 'data/'
base_csv = os.path.join(base_dir, 'dataset.csv')
base_codes = os.path.join(base_dir, 'code/')

src_dir = 'src/dataset-creator/data/'
src_csv = os.path.join(src_dir, 'dataset.csv')
src_codes = os.path.join(src_dir, 'code/')

# 2. Przetwarzanie plików CSV w celu znalezienia duplikatów
print("Przetwarzanie i łączenie plików dataset.csv...")
df_base = pd.read_csv(base_csv)
df_src = pd.read_csv(src_csv)

prefix = 'merge_3_'

# Dodanie przedrostka 'merge_' do nazw plików z folderu przenoszonego
df_src['code_file'] = prefix + df_src['code_file'].astype(str)

# Łączenie w jeden duży DataFrame
df_combined = pd.concat([df_base, df_src], ignore_index=True)

# Usuwamy duplikaty na podstawie: topic, instruction, code
df_deduplicated = df_combined.drop_duplicates(
    subset=['topic', 'instruction', 'code'], 
    keep='first'
).copy() # robimy kopię, żeby uniknąć błędów nadpisywania w locie

# NAPRAWA ID: Nadajemy nowe, unikalne ID dla każdego wiersza po usunięciu duplikatów
df_deduplicated['id'] = range(len(df_deduplicated))

# Zapisujemy odfiltrowany dataset z naprawionym ID
df_deduplicated.to_csv(base_csv, index=False)
print(f"Zapisano {base_csv}. Zredukowano z {len(df_combined)} do {len(df_deduplicated)} wierszy. Zaktualizowano ID.")

# Tworzymy zbiór (set) dozwolonych plików - nasza "biała lista"
valid_files = set(df_deduplicated['code_file'].tolist())

# 3. Przenoszenie kodów i usuwanie zduplikowanych z folderu źródłowego
print("Przenoszenie plików i usuwanie duplikatów z src/...")
if os.path.exists(src_codes):
    for filename in os.listdir(src_codes):
        src_file_path = os.path.join(src_codes, filename)
        
        if os.path.isfile(src_file_path):
            new_filename = prefix + filename
            dest_file_path = os.path.join(base_codes, new_filename)
            
            # Sprawdzamy, czy plik z nową nazwą przetrwał deduplikację
            if new_filename in valid_files:
                # To nie jest duplikat -> przenosimy
                shutil.move(src_file_path, dest_file_path)
            else:
                # To JEST duplikat -> kasujemy go z dysku
                os.remove(src_file_path)

# 4. Czyszczenie folderu głównego (data/codes/) z ewentualnych starych duplikatów
print("Czyszczenie folderu docelowego z osieroconych plików...")
if os.path.exists(base_codes):
    for filename in os.listdir(base_codes):
        file_path = os.path.join(base_codes, filename)
        
        if os.path.isfile(file_path):
            # Jeżeli jakiegoś pliku .py nie ma już w nowym CSV, usuń go z dysku
            if filename not in valid_files:
                os.remove(file_path)

print("Gotowe! Skrypt połączył dane, usunął duplikaty, odświeżył indeksy ID i wyczyścił foldery z kodami.")