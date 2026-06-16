import asyncio
from typing import List, Dict, Any
async def process_branch_a(data: str) -> Dict[str, Any]:
    return {"branch": "A", "status": "completed", "data_length": len(data)}
async def process_branch_b(items: List[int]) -> Dict[str, Any]:
    total = sum(items)
    avg = total / len(items) if items else 0.0
    return {"branch": "B", "status": "completed", "total_sum": total, "average_value": round(avg, 2)}
async def process_branch_c(text: str) -> Dict[str, Any]:
    word_count = len(text.split())
    char_count = len(text)
    return {"branch": "C", "status": "completed", "word_count": word_count, "char_count": char_count}
async def main():
    tasks: List[asyncio.Task] = []
    task_a = asyncio.create_task(process_branch_a("Hello World"))
    task_b = asyncio.create_task(process_branch_b([10, 20, 30]))
    task_c = asyncio.create_task(process_branch_c("Python is awesome"))
    tasks.append(task_a)
    tasks.append(task_b)
    tasks.append(task_c)
    results: List[Dict[str, Any]] = await asyncio.gather(*tasks)
    for result in results:
        print(result)
if __name__ == '__main__':
    asyncio.run(main())