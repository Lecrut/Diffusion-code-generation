import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
def fetch_name_from_api(coord):
    try:
        response = f"Name_{coord[0]}_{coord[1]}"                                
        return coord, response
    except Exception:
        raise RuntimeError(f"API failure for {coord}")
def bulk_coordinate_to_name(coords):
    if not coords or len(coords) == 0:
        return []
    x_coords = np.array([c[0] for c in coords])
    y_coords = np.array([c[1] for c in coords])
    results = {}
    try:
        batch_size = 10
        start_time = time.time()
        for i in range(0, len(coords), batch_size):
            end_idx = min(i + batch_size, len(coords))
            current_batch = coords[i:end_idx]
            if isinstance(current_batch[0], (list, tuple)):
                x_b = np.array([c[0] for c in current_batch])
                y_b = np.array([c[1] for c in current_batch])
                mock_names = [f"Vector_{x}_{y}" for x, y in zip(x_b.tolist(), y_b.tolist())]
            else:
                raise ValueError("Coordinates must be tuples or lists")
            results.update(zip(current_batch, mock_names))
        elapsed_time = time.time() - start_time
    except Exception as e:
        print(f"Vectorized operation failed. Falling back to sequential mode due to error: {e}")
        results_fallback = {}
        with ThreadPoolExecutor(max_workers=5) as executor:
            future_to_coord = {executor.submit(fetch_name_from_api, coord): coord for coord in coords}
            for future in as_completed(future_to_coord):
                try:
                    result = future.result()
                    results_fallback[result[0]] = result[1]
                except Exception as exc:
                    if isinstance(exc.__cause__, RuntimeError) and "API failure" in str(exc.__cause__):
                        pass
        return list(results_fallback.values())
if __name__ == '__main__':
    sample_coords = [(1.0, 2.0), (3.0, 4.0), (5.0, 6.0)]
    coords_to_process = [list(c) for c in sample_coords]
    names_list = bulk_coordinate_to_name(coords_to_process)
    print("Generated Names:", names_list)