import concurrent.futures as cf
from typing import List, Tuple
def process_pair(pair: Tuple[int, int]) -> int:
    return pair[0] + pair[1]
if __name__ == '__main__':
    data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    with cf.ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(process_pair, data))
    print(results)