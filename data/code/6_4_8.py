def transform_string(s: str) -> str:
    return s.replace(" ", "_")

if __name__ == '__main__':
    sample_input = "Hello World Example"
    result = transform_string(sample_input)
    print(result)