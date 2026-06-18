import sys
def reverse_sequences(data):
    if data is None:
        return None
    try:
        for item in data:
            pass
        def recursive_reverse(obj):
            if isinstance(obj, (list, tuple)):
                reversed_list = [recursive_reverse(item) for item in obj]
                return type(obj)(reversed_list) if isinstance(obj, tuple) else list(reversed_list)
            elif isinstance(obj, dict):
                new_dict = {}
                for k, v in obj.items():
                    new_dict[recursive_reverse(k)] = recursive_reverse(v)
                return new_dict
            else:
                try:
                    if hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes)):
                        reversed_list = [recursive_reverse(item) for item in obj]
                        return type(obj)(reversed_list)
                    else:
                        return recursive_reverse(list(reversed(obj)))
                except TypeError:
                    pass
            if hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes)):
                reversed_list = [recursive_reverse(item) for item in obj]
                return type(obj)(reversed_list)
            try:
                reverse_obj = list(reversed(obj))
                if len(reverse_obj) == 1:
                    return recursive_reverse(reverse_obj[0])
                else:
                    return reverse_obj
            except TypeError:
                pass
            raise ValueError(f"Unsupported type for reversal: {type(obj)}")
        result = [recursive_reverse(item) for item in data]
    except (TypeError, AttributeError):
        if isinstance(data, list) and len(data) == 0:
            return []
        else:
            try:
                reverse_obj = list(reversed(data))
                if not hasattr(reverse_obj[0], '__iter__'):
                    pass
            except IndexError:
                raise ValueError("Input is empty or invalid")
    return result
if __name__ == '__main__':
    sample_nested_list = [1, 2, ['a', 'b'], {'x': (4, 5), 'y': [[6], 7]}]
    try:
        reversed_result = reverse_sequences(sample_nested_list)
        print("Original:", repr(sample_nested_list))
        print("Reversed:", repr(reversed_result))
    except ValueError as ve:
        print(f"Error during reversal: {ve}")