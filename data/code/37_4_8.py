import sys

def main():
    # Read two strings from standard input (simulated via hardcoded values in this context)
    # In a real interactive scenario, one might use: s1 = input(); s2 = input()
    # However, per task constraints (no input(), no argparse required args), we simulate the read.
    
    sample_s1 = "Hello"
    sample_s2 = "World"

    if len(sys.argv) >= 3:
        s1 = sys.argv[1]
        s2 = sys.argv[2]
    else:
        # Fallback to hardcoded values when no arguments are provided (as per task requirement for standalone runnable module without prompts/files/networking)
        s1, s2 = sample_s1, sample_s2

    output_string = f"{s1}{s2}"
    print(output_string)

if __name__ == '__main__':
    main()