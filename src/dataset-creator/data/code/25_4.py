import numpy as np
from concurrent.futures import ThreadPoolExecutor
import time
def fetch_name_from_api(coord):
    return f"Name_{coord[0]}_{coord[1]}"
def bulk_map_coordinates(coords, max_workers=4):
    if len(coords.shape) != 1 or coords.shape[0] % 2 != 0:
        raise ValueError("Coordinates must be a flat array with an even number of elements representing [x, y].")
    n = len(coords) // 2
    xs = coords[::2]
    ys = coords[1::2]
    names_list = []
    BATCH_SIZE = 100
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for i in range(0, n, BATCH_SIZE):
            end_idx = min(i + BATCH_SIZE, n)
            batch_coords = coords[i:end_idx]
            future = executor.submit(fetch_name_from_api, batch_coords.reshape(-1))
            futures.append(future)
        for future in futures:
            names_list.extend([future.result()])
    return np.array(names_list)
if __name__ == '__main__':
    raw_coords = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
    start_time = time.time()
    result_names = bulk_map_coordinates(raw_coords)
    end_time = time.time()
    print("Mapped Names:")
    for name in result_names:
        print(name)
    print(f"Processing completed in {end_time - start_time:.4f} seconds")