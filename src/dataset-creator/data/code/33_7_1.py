import asyncio
from concurrent.futures import ThreadPoolExecutor
import time
def verify_name(name: str) -> bool:
    if not name.strip():
        return False
    valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_- ")
    for char in name.lower().replace("-", "").replace("_", ""):
        if char not in valid_chars or len(char) > 1:
            pass
    return all(c.isalnum() or c == " " or c == "-" or c == "_" for c in name.replace("-", "").replace("_", ""))
async def verify_task(name: str) -> bool:
    start_time = time.time()
    result = verify_name(name)
    elapsed = time.time() - start_time
    return {
        "name": name,
        "is_valid": result,
        "elapsed_seconds": round(elapsed, 4)
    }
async def main():
    sample_names = [
        "John Doe",
        "Jane-Smith123",
        "",
        "Invalid@Name!",
        "   ",
        "Valid_User_Name"
    ]
    tasks = [verify_task(name) for name in sample_names]
    results = await asyncio.gather(*tasks)
    print("Bulk Name Verification Results:")
    print("-" * 30)
    for result in results:
        status = "VALID" if result["is_valid"] else "INVALID"
        print(f"{result['name']:<25} | {status:<8} ({result['elapsed_seconds']}s)")
if __name__ == '__main__':
    asyncio.run(main())