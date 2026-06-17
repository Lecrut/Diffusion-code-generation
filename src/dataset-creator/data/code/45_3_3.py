import concurrent.futures as cf
def process_pair(pair):
    return sum(pair)
pairs = [[10, 20], [30, 40], [50, 60]]
if __name__ == '__main__':
    with cf.ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(process_pair, pairs))
    print(results)