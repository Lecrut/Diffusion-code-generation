import sys

def compare_integers(a: int, b: int) -> str:
    """Compare two integers and return a descriptive message."""
    if a > b:
        msg = f"{a} is larger than {b}"
    elif a < b:
        msg = f"{b} is larger than {a}"
    else:
        msg = "Both numbers are equal"
    return msg

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    val1, val2 = 42, 50
    
    result_msg = compare_integers(val1, val2)
    
    print(result_msg)