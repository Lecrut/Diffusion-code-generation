import concurrent.futures as cf
def process_pair(pair):
    return pair[0] + pair[1]
if __name__ == '__main__':
    data = [(5, 3), (10, -2), (7, 8), (99, 1)]
    with cf.ThreadPoolExecutor() as executor:
        results = list(executor.map(process_pair, data))
    print(results)