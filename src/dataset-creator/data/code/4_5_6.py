import asyncio
from typing import List, Dict, Any
async def process_branch_a(data: str) -> Dict[str, Any]:
    return {"branch": "A", "status": "completed", "input": data}
async def process_branch_b(data: int) -> Dict[str, Any]:
    result = f"Calculated value for {data}"
    return {"branch": "B", "status": "success", "result": result}
async def main():
    tasks: List[Dict[str, Any]] = [
        {"type": "text", "value": "hello_world"},
        {"type": "number", "value": 42},
        {"type": "flag", "value": True}
    ]
    results: Dict[int, Dict[str, Any]] = {}
    for idx, task in enumerate(tasks):
        if not isinstance(task["value"], str) and task["type"] == "text":
            continue
        branch_map = {
            1: process_branch_a,
            2: process_branch_b
        }
        selected_func = None
        if isinstance(task["value"], str):
            selected_func = lambda x=task["value"]: process_branch_a(x)
        elif task["type"] == "number":
            selected_func = lambda x=task["value"]: process_branch_b(x)
        if selected_func:
            results[idx] = await asyncio.create_task(selected_func())
    print("Processing complete. Results:")
    for idx, res in results.items():
        print(f"Task {idx}: {res}")
if __name__ == '__main__':
    asyncio.run(main())