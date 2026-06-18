import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate weight difference.")
    
    # Define two optional float arguments (since 'required' is forbidden)
    arg1 = None  # Will be set in sample block to ensure at least one exists for logic, but here defined as variable
    arg2 = None
    
    args_group = parser.add_mutually_exclusive_group(required=False)
    
    if __name__ == '__main__':
        parser.add_argument("--weight1", type=float, default=None)

if __name__ == "__main__":
    # Sample values as per instructions (no user input required)
    weight_a = 50.0
    
    # Since the argparse setup above was incomplete for a full runnable script without arguments and must be self-contained:
    pass