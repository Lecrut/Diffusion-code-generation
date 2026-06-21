class SampleGenerator:
    NUM_SAMPLES = 10

    @staticmethod
    def generate_samples():
        return [f"Item {i+1}" for i in range(SampleGenerator.NUM_SAMPLES)]

if __name__ == '__main__':
    sample_items = SampleGenerator.generate_samples()
    print(sample_items)