import json
import matplotlib.pyplot as plt
from pathlib import Path

# Set up paths relative to the report directory
report_dir = Path(__file__).parent.resolve()
best_results_dir = (report_dir / "../best_results").resolve()
figures_dir = (report_dir / "figures").resolve()
figures_dir.mkdir(parents=True, exist_ok=True)

# Set styling for plots
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.titlesize': 14,
    'font.family': 'sans-serif'
})

def load_data(filename):
    path = best_results_dir / filename
    data = json.loads(path.read_text(encoding="utf-8"))
    return data[0]['x'], data[0]['y']

# Plot 1: Validation Loss at different masking rates
fig, ax = plt.subplots(figsize=(8, 5), dpi=300)

x_all, y_overall = load_data("val_loss VS step_chart_data (4).json")
x25, y25 = load_data("val_loss_mask_25 VS step_chart_data (2).json")
x50, y50 = load_data("val_loss_mask_50 VS step_chart_data (2).json")
x75, y75 = load_data("val_loss_mask_75 VS step_chart_data (1).json")
x95, y95 = load_data("val_loss_mask_95 VS step_chart_data (3).json")

ax.plot(x_all, y_overall, label='Strata ogólna (średnia)', color='#2c3e50', linewidth=2)
ax.plot(x25, y25, label='Maska 25%', color='#2ecc71', linewidth=1.5, linestyle='--')
ax.plot(x50, y50, label='Maska 50%', color='#3498db', linewidth=1.5, linestyle='-.')
ax.plot(x75, y75, label='Maska 75%', color='#f1c40f', linewidth=1.5, linestyle=':')
ax.plot(x95, y95, label='Maska 95%', color='#e74c3c', linewidth=1.5, linestyle='-')

ax.set_title('Ewolucja straty walidacyjnej (Validation Loss)')
ax.set_xlabel('Krok treningowy (Step)')
ax.set_ylabel('Wartość straty (Loss)')
ax.legend(frameon=True, facecolor='white', framealpha=0.9)
ax.set_xlim(0, max(x_all))
ax.set_ylim(0, 12)

plt.tight_layout()
fig.savefig(figures_dir / "val_loss_masking.pdf", format='pdf')
fig.savefig(figures_dir / "val_loss_masking.png", format='png')
plt.close(fig)

# Plot 2: Prompt Shuffling Analysis
fig, ax = plt.subplots(figsize=(8, 5), dpi=300)

x_shuf, y_shuf = load_data("val_prompt_shuffle_loss_mask_100 VS step_chart_data (1).json")
x_delta, y_delta = load_data("val_prompt_shuffle_loss_delta_mask_100 VS step_chart_data (1).json")

# original_loss = shuffle_loss - delta
y_orig = [s - d for s, d in zip(y_shuf, y_delta)]

ax.plot(x_shuf, y_shuf, label='Strata przy pomylonym kontekście (Shuffled Prompt)', color='#c0392b', linewidth=2)
ax.plot(x_shuf, y_orig, label='Strata przy poprawnym kontekście (Original Prompt)', color='#27ae60', linewidth=2)
ax.plot(x_delta, y_delta, label='Różnica straty (Delta)', color='#8e44ad', linewidth=1.5, linestyle=':')

ax.set_title('Wpływ wymieszania kontekstu (Prompt Shuffling) na stratę (Maska 100%)')
ax.set_xlabel('Krok treningowy (Step)')
ax.set_ylabel('Wartość straty (Loss)')
ax.legend(frameon=True, facecolor='white', framealpha=0.9)
ax.set_xlim(0, max(x_shuf))
ax.set_ylim(0, 12)

plt.tight_layout()
fig.savefig(figures_dir / "val_prompt_shuffle.pdf", format='pdf')
fig.savefig(figures_dir / "val_prompt_shuffle.png", format='png')
plt.close(fig)

# Plot 3: Generation Dynamics (remasked tokens per step)
fig, ax = plt.subplots(figsize=(8, 5), dpi=300)

x_rem, y_rem = load_data("val_generation_remasked_tokens_per_step VS step_chart_data (1).json")

ax.plot(x_rem, y_rem, color='#d35400', linewidth=2, label='Liczba remaskowanych tokenów')
ax.set_title('Dynamika generowania: Liczba remaskowanych tokenów na krok')
ax.set_xlabel('Krok treningowy (Step)')
ax.set_ylabel('Średnia liczba remaskowanych tokenów')
ax.set_xlim(0, max(x_rem))
ax.set_ylim(0, max(y_rem) * 1.1)
ax.legend(frameon=True, facecolor='white', framealpha=0.9)

plt.tight_layout()
fig.savefig(figures_dir / "val_generation_remasking.pdf", format='pdf')
fig.savefig(figures_dir / "val_generation_remasking.png", format='png')
plt.close(fig)

print("Generated plots successfully.")
