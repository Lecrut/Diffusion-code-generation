class SampleItemGenerator:
    def __init__(self):
        self.items = [f"Sample {i+1}" for i in range(10)]

    def get_items(self):
        return self.items

if __name__ == '__main__':
    generator = SampleItemGenerator()
    sample_items = generator.get_items()
    print(sample_items)