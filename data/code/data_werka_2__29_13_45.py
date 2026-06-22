def reverse_string(s):
    return ''.join(reversed(s))

class StringManipulator:
    DEFAULT_SAMPLE = "Hello, World!"
    
    @staticmethod
    def process_samples(samples):
        results = {}
        for sample in samples:
            reversed_sample = reverse_string(sample)
            results[sample] = reversed_sample
        return results

if __name__ == '__main__':
    sample_values = [
        StringManipulator.DEFAULT_SAMPLE,
        "12345",
        "Python"
    ]
    manipulator = StringManipulator()
    reversed_samples = manipulator.process_samples(sample_values)
    for original, reversed_value in reversed_samples.items():
        print(f"Original: {original} -> Reversed: {reversed_value}")