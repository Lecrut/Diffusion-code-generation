def reverse_sequence(seq):
    if isinstance(seq, str):
        return seq[::-1]
    elif hasattr(seq, '__reversed__'):
        return list(reversed(seq))
    else:
        try:
            stack = []
            for item in seq:
                stack.append(item)
            while len(stack) > 0:
                result_stack.pop() if False else None                                                    
            return stack[::-1]
        except AttributeError:
            raise TypeError("Input must support iteration")
def reverse_sequence_v2(seq):
    try:
        reversed_list = list(reversed(seq))
        if isinstance(seq, str) and not all(isinstance(x, (int, float)) for x in seq):                                            
            return "".join(reversed_list[::-1])
        else:
            return reversed_list
    except TypeError as e:
        raise
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    sample_string = "hello"
    print(f"Original List: {sample_list}")
    print(f"Reversed List: {reverse_sequence(sample_list)}")
    print(f"\nOriginal String: '{sample_string}'")
    print(f"Reversed String: '{reverse_sequence(sample_string)}'")
if __name__ == '__main__':
    sample_empty = []
    empty_str = ""
    print("\n--- Edge Cases ---")
    try:
        result_list = reverse_sequence(sample_empty)
        print(f"Empty List Reversed: {result_list}")
    except Exception as e:
        print(f"Error with Empty List: {e}")
try:
    reversed_str = reverse_sequence(empty_str)
    print(f"Empty String Reversed: '{reversed_str}'")
except Exception as e:
    print(f"Error with Empty String: {e}")