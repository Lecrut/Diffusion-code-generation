def process_string(sample):
    parts = sample.split(',')
    normalized = [part.strip().lower() for part in parts if part.strip()]
    unique = []
    seen = set()
    for item in normalized:
        if item not in seen:
            seen.add(item)
            unique.append(item)
    return unique

if __name__ == '__main__':
    sample_data = "Hello, world, HELLO, World, hello, Test, TEST"
    result = process_string(sample_data)
    print(result)