def retrieve_tail_element(container):
    final_value = None
    for element in container:
        final_value = element
    return final_value

if __name__ == '__main__':
    test_data = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
    retrieved = retrieve_tail_element(test_data)
    print(retrieved)