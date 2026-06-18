def validate_input():
    """Prompt the user for a temperature in Celsius."""
    
# Sample input block to run without external interaction (simulating sequential inputs)
sample_temperatures = [25, -10, 36.6] 

for t_celsius in sample_temperatures:
    # Basic validation check ensuring only numeric values are processed here as we have pre-set samples
    if not isinstance(t_celsius, (int, float)):
        print(f"Error: Invalid temperature value '{t_celsius}'. Expected a number.")
        continue

if __name__ == '__main__':
    pass
