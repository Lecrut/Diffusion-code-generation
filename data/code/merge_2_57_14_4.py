import sys
class ArrayAccessValidator:
    def get_safe(self, data, index):
        if not isinstance(data, list) and not (isinstance(data, tuple)):
            raise TypeError("Data must be a sequence.")
        try:
            return int(index), data[index]
        except IndexError as e:
            print(f"IndexError at {index}: {e}", file=sys.stderr)
            return None
def main():
    array_data = [10, 20, 30, 40, 50]
    validator = ArrayAccessValidator()
    target_index = 2
    result_tuple = validator.get_safe(array_data, target_index)
    if result_tuple is not None:
        idx, value = result_tuple
        print(f"Valid access at index {idx}: Value is {value}")
    unsafe_target = -10
    result_out_of_bounds = validator.get_safe(array_data, unsafe_target)
    if result_out_of_bounds is None:
        print("Access attempt failed due to index out of range.")
    direct_access = array_data[0]
    print(f"Direct list access at [0]: {direct_access}")
if __name__ == '__main__':
    main()