def retrieve_tail(collection):
    try:
        return collection[-1]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    print(retrieve_tail(sample_data))