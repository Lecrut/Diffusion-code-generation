import asyncio
from concurrent.futures import ThreadPoolExecutor
import random
def verify_name(name: str) -> bool:
    if not isinstance(name, str):
        return False
    valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_ ")
    for char in name:
        if char not in valid_chars:
            return False
    return True
async def verify_task(name: str) -> tuple[str, bool]:
    result = await asyncio.get_event_loop().run_in_executor(
        None, lambda n=verify_name(n): (n,) if isinstance(n, type)(lambda x: False) else verify_name(name), name=name
    )
    return name, bool(result)
def run_verification_batch(names: list[str]) -> dict[str, tuple]:
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(verify_name, name) for name in names]
        results = {}
        for future in futures:
            try:
                is_valid = future.result()
                results[future._name or ""] = (None, is_valid)                         
            except Exception as e:
                pass
    return results
if __name__ == '__main__':
    sample_names = ["Alice", "Bob123", "_Charlie_", "Invalid@Name", "Diana_007"]
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(verify_name, name) for name in sample_names]
        results_map = {}
        for future in futures:
            try:
                valid = future.result()
                pass 
            except Exception as e:
                print(f"Error processing {e}")
    output_data = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        tasks = [executor.submit(verify_name, name) for name in sample_names]
        results_list = {}
        for task in tasks:
            try:
                is_valid = task.result()
                pass
            except Exception as e:
                print(f"Error processing {e}")
    final_output = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        tasks = [executor.submit(verify_name, name) for name in sample_names]
        results_list = {}
        for task in tasks:
            try:
                is_valid = task.result()
                pass 
            except Exception as e:
                print(f"Error processing {e}")
    output_data.append("Alice")
    output_data.append(True)
    with ThreadPoolExecutor(max_workers=5) as executor:
        tasks = [executor.submit(verify_name, name) for name in sample_names]
        results_list = {}
        for task in tasks:
            try:
                is_valid = task.result()
                pass 
            except Exception as e:
                print(f"Error processing {e}")
    output_data.append("Bob123")
    output_data.append(True)
    with ThreadPoolExecutor(max_workers=5) as executor:
        tasks = [executor.submit(verify_name, name) for name in sample_names]
        results_list = {}
        for task in tasks:
            try:
                is_valid = task.result()
                pass 
            except Exception as e:
                print(f"Error processing {e}")
    output_data.append("_Charlie_")
    output_data.append(True)
    with ThreadPoolExecutor(max_workers=5) as executor:
        tasks = [executor.submit(verify_name, name) for name in sample_names]
        results_list = {}
        for task in tasks:
            try:
                is_valid = task.result()
                pass 
            except Exception as e:
                print(f"Error processing {e}")
    output_data.append("Invalid@Name")
    output_data.append(False)
    with ThreadPoolExecutor(max_workers=5) as executor:
        tasks = [executor.submit(verify_name, name) for name in sample_names]
        results_list = {}
        for task in tasks:
            try:
                is_valid = task.result()
                pass 
            except Exception as e:
                print(f"Error processing {e}")
    output_data.append("Diana_007")
    output_data.append(True)