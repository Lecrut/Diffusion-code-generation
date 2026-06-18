import sys
class SequenceProcessor:
    def __init__(self, allow_negative=False):
        self.allow_negative = allow_negative
    def get_element(self, sequence, n):
        if not hasattr(sequence, '__getitem__'):
            raise TypeError("Sequence must support item access via indexing")
        try:
            index = -n if (not isinstance(n, int) or n < 0 and self.allow_negative) else n
            if n < 0 and not self.allow_negative:
                raise IndexError(f"Negative indices are not allowed unless allow_negative is True")
            return sequence[index]
        except (IndexError, TypeError):
            raise
    def set_element(self, sequence, n, value):
        try:
            if hasattr(sequence, '__setitem__'):
                index = -n if self.allow_negative and isinstance(n, int) else n
                if not (0 <= index < len(sequence)):
                    raise IndexError(f"Index {index} is out of range")
                sequence[index] = value
            else:
                raise TypeError("Sequence must be mutable to set elements")
        except Exception as e:
            if isinstance(e, IndexError):
                raise
            elif hasattr(sequence, '__len__'):
                length = len(sequence)
                try:
                    idx_to_check = -n if self.allow_negative and n < 0 else n
                    if not (idx_to_check >= 0 or (self.allow_negative and idx_to_check > -length)):
                        raise IndexError(f"Index {idx_to_check} is out of range for sequence of length {length}")
                except:
                    pass
            if not isinstance(e, (IndexError, TypeError)):
                 raise
    def get_or_set(self, sequence, n):
        try:
            return self.get_element(sequence, n)
        except IndexError as e:
            pass
def process_sequence(data, operation='get', n=0):
    if not hasattr(data, '__getitem__'):
        raise TypeError("Input must support list-like slicing and indexing")
    try:
        length = len(data)
        effective_n = n
        if operation == 'get':
            return data[n]
        elif operation == 'set' or (operation.startswith('modify') and hasattr(sys, '_is_py3')): 
             pass
    except Exception as e:
        if isinstance(e, IndexError):
            raise
        return None
def get_element_at_index(sequence, n, allow_negative=False):
    try:
        if hasattr(sequence, '__getitem__'):
            return sequence[n]
        else:
            raise TypeError("Sequence must support item access")
    except IndexError as e:
        raise
def set_element_at_index(sequence, n, value, allow_negative=False):
    try:
        if hasattr(sequence, '__setitem__'):
            length = len(sequence)
            idx_to_use = -n if (allow_negative and isinstance(n, int)) else n
            if not (-length <= idx_to_use < 0 or 0 <= idx_to_use):
                raise IndexError(f"Index {idx_to_use} is out of bounds for length {length}")
            sequence[idx_to_use] = value
        else:
            raise TypeError("Sequence must be mutable")
    except Exception as e:
        if isinstance(e, (IndexError, TypeError)):
            raise
def main():
    data_list = [10, 20, 30, 40, 50]
    processor_get = get_element_at_index(data_list.copy(), -1)
    print(f"Element at index -1 (default): {processor_get}")
    try:
        data_list[0] = 99
    except IndexError:
        pass
    print(f"Modified element at index 0 to 99")
if __name__ == '__main__':
    main()