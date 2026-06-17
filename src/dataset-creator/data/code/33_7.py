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
async def verify_task(name: str) -> dict:
    result = await asyncio.to_thread(verify_name, name)
    return {"name": name, "is_valid": result}
def run_bulk_verification(names):
    loop = asyncio.new_event_loop()
    executor = ThreadPoolExecutor(max_workers=10)
    async def main():
        tasks = [verify_task(name) for name in names]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        final_results = []
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                final_results.append({"name": names[i], "is_valid": False, "error": str(result)})
            else:
                final_results.append(result)
        return final_results
    try:
        results = loop.run_until_complete(main())
    finally:
        executor.shutdown(wait=False)
    return results
if __name__ == '__main__':
    sample_names = [
        "John Doe",
        "Jane_Doe123",
        "Invalid!@#",
        "",
        "Bob Smith Jr.",
        "Alice_098"
    ]
    verification_results = run_bulk_verification(sample_names)
    for result in verification_results:
        print(f"{result['name']}: {'Valid' if result.get('is_valid') else 'Invalid'}")