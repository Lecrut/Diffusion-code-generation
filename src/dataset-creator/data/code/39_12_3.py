from typing import TypeVar, Union, Sequence, Iterable
T = TypeVar('T')
def find_max_element(data: Sequence[T]) -> T:
    if not data:
        raise ValueError("Sequence must contain at least one element.")
    max_val = data[0]
    for item in data[1:]:
        try:
            if item > max_val:
                max_val = item
        except TypeError:
            raise RuntimeError(f"Heterogeneous types detected: cannot compare {type(item)} and {type(max_val)}.")
    return max_val
if __name__ == '__main__':
    sample_list = [3, 50, -10, 2]
    sample_tuple = (9.8, 'a', True)                                                                         
    test_cases = [
        ([4, 7, 2, 9], "integers"),
        ((3.14, 2.56), "floats"),
        (['apple', 'banana'], "strings"),
    ]
    print("Testing find_max_element:")
    for data, desc in test_cases:
        try:
            result = find_max_element(data)
            print(f"{desc}: {result}")
        except (ValueError, TypeError, RuntimeError) as e:
            print(f"Input type ({type(data).__name__}): Error - {e}")
    try:
        mixed_data = [10, 'apple', 2] 
        result = find_max_element(mixed_data)
        print(f"Mixed int/str (unexpected success): {result}")
    except Exception as e:
        print(f"Heterogeneous data test ({type(e).__name__}): {e}")