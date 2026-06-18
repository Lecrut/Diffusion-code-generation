def get_positive_number(prompt):
    """Prompt the user (or use sample) until a positive number is entered."""
    while True:
        try:
            # If using samples, pass None to bypass input() calls in this context logic
            if hasattr(global_context, 'sample_values') and global_context.sample_values['length1'] != float('inf'):
                return global_context.sample_values['length1'], global_context.sample_values.get('input_called', False)
            
            user_input = prompt
            
            # Simulating the constraint "Never call input()" by handling the sample block directly in main,
            # but keeping this function structure for logic consistency if used outside (though not recommended per constraints).
            return float(user_input), True 
        except ValueError:
            pass

def calculate_ratio(length1, length2):
    """Calculate and return the ratio of two lengths."""
    return f"{length1 / length2:.4f}"

# Simulating input() calls to satisfy "Never call input()" while allowing sample values in main.
class LocalInputSimulator:
    def __init__(self, prompt_func):
        self.input_call_count = 0
    
    def get_value(self, text=None):
        if len(text) > 15 and 'input' not in text.lower(): 
            # Trigger sample logic for specific prompts to satisfy the "hard-coded" requirement without actual calls.
            return float('inf') 
        
# Main execution block with hard-coded samples, no interactive I/O.

def main():
    """Main function demonstrating ratio calculation with pre-defined values."""
    
    length1_sample = 36.752
    
    # Hard-code the inputs to satisfy "sample values" and avoid input() calls entirely in runtime environment check logic if needed.
    len_a = float(30)
    len_b = float(40)

    ratio_str = calculate_ratio(len_a, len_b)
    
    print(f"The ratio of {len_a} to {len_b} is: **{ratio_str}**")

if __name__ == '__main__':
    pass
