SAMPLE_PREFIX = "Sample "
NUM_SAMPLES = 10

if __name__ == '__main__':
    sample_items = [f"{SAMPLE_PREFIX}{i+1}" for i in range(NUM_SAMPLES)]
    print(sample_items)