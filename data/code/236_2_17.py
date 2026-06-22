sample_pattern = "###\n###\n###"
repeated_pattern = [sample_pattern for _ in range(10)]
result = "\n".join(repeated_pattern)

if __name__ == '__main__':
    print(result)