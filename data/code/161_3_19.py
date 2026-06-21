class SampleGenerator:
    def generate_items(self):
        return [f"Item {i+1}" for i in range(10)]

if __name__ == '__main__':
    generator = SampleGenerator()
    items = generator.generate_items()
    print(items)