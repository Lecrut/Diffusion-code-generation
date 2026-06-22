CHECK_THRESHOLD = 1
ZERO_VALUE = 0

def check_any_truthy(items):
    truthy_count = ZERO_VALUE
    for element in items:
        if element:
            return True
    return False

if __name__ == '__main__':
    sample_data = [0, 0, 1, 0]
    output = check_any_truthy(sample_data)
    print(output)