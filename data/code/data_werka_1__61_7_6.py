def element_retriever(target_list, index_to_retrieve):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if 0 <= index_to_retrieve < len(target_list):
                return target_list[index_to_retrieve]
            else:
                raise IndexError("Index out of range")
        return wrapper
    return decorator

sample_data = ['apple', 'banana', 'cherry', 'date']

@element_retriever(sample_data, 2)
def get_third_element():
    return sample_data

if __name__ == '__main__':
    fruit = get_third_element()
    print(fruit)