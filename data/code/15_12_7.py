INDEXING_CONFIG = {
    "target": -2
}

def get_penultimate(list_input):
    return list_input[INDEXING_CONFIG["target"]]

if __name__ == '__main__':
    test_values = [100, 200, 300, 400]
    final_output = get_penultimate(test_values)
    print(final_output)