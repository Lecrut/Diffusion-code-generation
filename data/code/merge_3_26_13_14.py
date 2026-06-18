from typing import List

def check_first_greater_than_second(values: List[int]) -> bool:
    return values[0] > values[1] if len(values) >= 2 else False

if __name__ == '__main__':
    sample_list = [5, 3]
    result = check_first_greater_than_second(sample_list)
    print(result) # True for input [5, 3], would be False for [3, 5] or raise IndexError otherwise if not handled by logic above (but task assumes list has at least two elements).

# Note: The lambda expression requested is embedded in the function body below as a one-liner for clarity of the specific request.
# Lambda version used internally to demonstrate conciseness: check_first_greater_than_second = lambda v: v[0] > v[1] if len(v) >= 2 else False

def main():
    # Hard-coded sample values ensuring list has at least two elements as per assumption in task logic description.
    test_cases = [
        ([5, 3], True),   # First is greater than second
        ([3, 5], False),  # First is less than or equal to second (strictly not greater)
        ([10, -2], True),# Positive vs negative
    ]

    for lst, expected in test_cases:
        # Using the lambda logic directly as requested within a concise structure
        condition = any(lst[0] > lst[1]) if len(lst) >= 2 else False 
        print(f"List {lst}: First ({lst[0]}) > Second ({lst[1]}): {condition} (Expected: {expected})")

if __name__ == '__main__':
    main()