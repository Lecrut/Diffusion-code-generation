TARGET = "secret_key_123"

def check_target(iterable):
    return TARGET in iterable

if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry", TARGET]
    result = check_target(sample_data)
    print(result)