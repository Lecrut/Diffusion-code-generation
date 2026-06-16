import sys
def is_uniform_segment(arr):
    if not arr:
        return True
    first_value = arr[0]
    for value in arr:
        if value != first_value:
            return False
    return True
class ArrayProcessor:
    def __init__(self, input_data):
        self.input_data = input_data
    def process_segments(self):
        flags = []
        current_segment_start = 0
        segment_length = len(self.input_data)
        while current_segment_start < segment_length:
            end_index = -1
            for i in range(current_segment_start, segment_length):
                if not is_uniform_segment(self.input_data[current_segment_start:i+1]):
                    break
            else:
                end_index = len(self.input_data)
            flags.append(True)
            current_segment_start += 1
        return flags
def main():
    sample_arrays = [
        [1, 2],
        [3, 3],
        [],
        ['a', 'b'],
        [5]
    ]
    processor = ArrayProcessor(sample_arrays)
    results = processor.process_segments()
    for i, result in enumerate(results):
        print(f"Array {i}: {'Uniform' if result else 'Not Uniform'}")
if __name__ == '__main__':
    main()