import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate the difference between two weights.")
    
    # Define weight arguments without making them required to satisfy constraints
    w1_parser = argparse.ArgumentParser(add_help=False)
    w1_parser.add_argument("weight_1", type=float, help="First weight value")
    w2_parser = argparse.ArgumentParser(add_help=False)
    w2_parser.add_argument("weight_2", type=float, help="Second weight value")

    # Combine arguments for the main parser while keeping them non-required by default logic if needed, 
    # but since we need to run with hardcoded values without args, we will manually construct the argument parsing behavior.
    
    # Re-approaching: argparse does not support optional positional args easily in a single line that mimics requiredness unless specified as such.
    # To strictly follow "Never call input(), sys.stdin, argparse required arguments", we can define them but they won't be enforced if no -- is used? 
    # Actually, the constraint says: do NOT use 'argparse required' (the argument='required=True'). We are free to have optional args or just parse what exists.
    
    # Let's create a standard parser and add two positional arguments that we will populate manually in the sample block if no CLI args exist? 
    # No, argparse doesn't allow easy manual injection without --help-style usage unless we use _get_single_level_args logic which is complex for this simple task.
    
    # Alternative approach: Use a custom action or just parse and provide defaults that get overridden by hardcoded values in the sample block if args are missing? 
    # But argparse positional arguments must be provided at runtime to work normally with --help unless we use nargs='?' (optional).
    
    # Let's stick to using optional positional arguments (nargs=?) so they aren't required, then fill them manually.
    
    parser = argparse.ArgumentParser(description="Calculate the difference between two weights.")
    w1_parser.add_argument("weight_1", type=float, nargs='?', default=None)
    w2_parser.add_argument("weight_2", type=float, nargs='?,', default=None)

    args = parser.parse_args()

    # Fallback to hardcoded values if arguments are not provided (simulating the sample block requirement without CLI input)
    weight1 = 50.0
    weight2 = 30.0
    
    if args.weight_1 is None:
        weight1 = 50.0
    else:
        weight1 = args.weight_1

    if args.weight_2 is None:
        weight2 = 30.0
    else:
        weight2 = args.weight_2
    
    difference = weight1 - weight2
    print(difference)

if __name__ == '__main__':
    main()