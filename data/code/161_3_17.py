class SampleGenerator:
    def __init__(self):
        self.sample_items = [f"Item {i+1}" for i in range(10)]

    def get_sample_items(self):
        return self.sample_items

if __name__ == '__main__':
    generator = SampleGenerator()
    sample_items = generator.get_sample_items()
    print(sample_items)