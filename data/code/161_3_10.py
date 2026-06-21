class SampleGenerator:
    def __init__(self):
        self.samples = [f"Sample {i+1}" for i in range(10)]

    def get_samples(self):
        return self.samples

if __name__ == '__main__':
    generator = SampleGenerator()
    print(generator.get_samples())