import sys

def compare_lengths(length1, length2):
    try:
        len1 = float(length1)
        len2 = float(length2)
        
        if len1 > len2:
            return f"{len1} is greater than {len2}"
        elif len1 < len2:
            return f"{len1} is less than {len2}"
        else:
            return f"{len1} is equal to {len2}"
    except ValueError:
        return "Invalid input: Please enter numeric values."

if __name__ == '__main__':
    length1 = '5.5'
    length2 = '3.2'
    
    result = compare_lengths(length1, length2)
    print(result)