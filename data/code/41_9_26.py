CASE_LOWER = 'lower'
CASE_UPPER = 'upper'
CASE_TITLE = 'title'
CASE_SWAP = 'swap'

def manipulate_case(s, case=CASE_LOWER):
    valid_cases = {CASE_LOWER, CASE_UPPER, CASE_TITLE, CASE_SWAP}
    
    if case not in valid_cases:
        raise ValueError(f"Invalid case specified: {case}. Choose from '{CASE_LOWER}', '{CASE_UPPER}', '{CASE_TITLE}', or '{CASE_SWAP}'.")
    
    case_functions = {
        CASE_LOWER: str.lower,
        CASE_UPPER: str.upper,
        CASE_TITLE: str.title,
        CASE_SWAP: str.swapcase
    }
    
    return case_functions[case](s)

if __name__ == '__main__':
    sample_string = 'Hello, World!'
    print(manipulate_case(sample_string, CASE_LOWER))
    print(manipulate_case(sample_string, CASE_UPPER))
    print(manipulate_case(sample_string, CASE_TITLE))
    print(manipulate_case(sample_string, CASE_SWAP))