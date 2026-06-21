SAMPLE_COUNT = 10

def generate_sample_items():
    return [f"Item {i+1}" for i in range(SAMPLE_COUNT)]

if __name__ == '__main__':
    sample_items = generate_sample_items()
    print(sample_items)