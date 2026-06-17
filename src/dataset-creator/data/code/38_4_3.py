import timeit
def initialize_and_populate():
    data = {}
    data['integers'] = [10, 20, 30]
    data['strings'] = ['hello', 'world', 'test']
    return data
if __name__ == '__main__':
    result = initialize_and_populate()
    assert isinstance(result['integers'], list) and all(isinstance(x, int) for x in result['integers'])
    assert isinstance(result['strings'], list) and all(isinstance(x, str) for x in result['strings'])
if __name__ == '__main__':
    print("Initialization complete.")