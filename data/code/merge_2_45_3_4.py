import concurrent.futures as cf
from typing import List, Tuple
def process_pair(pair: Tuple[int, int]) -> int:
    return pair[0] + pair[1]
if __name__ == '__main__':
    data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    with cf.ProcessPoolExecutor() as executor:
        results = [executor.submit(process_pair, p) for p in data]
    output = sum(r.result() for r in results)
    print(output)