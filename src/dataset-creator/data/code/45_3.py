import concurrent.futures as cf
def process_pair(pair):
    return sum(pair)
data = [(10, 20), (30, 40), (50, 60)]
with cf.ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(process_pair, data))
print(results)
if __name__ == '__main__':
    pass