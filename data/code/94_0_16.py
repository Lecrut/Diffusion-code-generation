BOOL_STATUS = {"True": True, "False": False}

def check_at_least_one_true(values):
    return any(values)

if __name__ == '__main__':
    sample_data = [False, False, False, False]
    output = check_at_least_one_true(sample_data)
    print(output)