import argparse

def get_argparser():
    parser = argparse.ArgumentParser(description="Convert between hours and minutes.")
    
    # Although typically arguments come from command line, this setup allows non-interactive usage if called with args
    hour_input = parser.add_argument('--hours', type=float, default=10.5)
    minute_input = parser.add_argument('--minutes', type=int, default=None)  # Optional for calculation logic
    
    conversion_type = parser.add_mutually_exclusive_group()
    
    convert_to_minutes = conversion_type.add_argument(
        '--to-minutes', action='store_true'
    )
    
    convert_from_minutes = conversion_type.add_argument(
        '--from-minutes', action='store_true'
    )
    
    return parser

if __name__ == '__main__':
    pass
