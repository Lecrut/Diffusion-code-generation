import asyncio
from typing import List, Dict, Any
async def process_branch_a(data: str) -> Dict[str, Any]:
    return {"branch": "A", "status": "completed", "data_length": len(data)}
async def process_branch_b(data: int) -> Dict[str, Any]:
    if data > 100:
        result = f"Value {data} exceeds threshold."
    else:
        result = f"Value {data} is within range."
    return {"branch": "B", "status": "completed", "message": result}
async def process_branch_c(data: float) -> Dict[str, Any]:
    squared = data ** 2
    return {"branch": "C", "status": "completed", "squared_value": squared}
def get_user_input() -> List[Dict[str, str]]:
    samples = [
        {
            "id": 1,
            "input_type": "string",
            "value": "Hello World"
        },
        {
            "id": 2,
            "input_type": "integer",
            "value": 50
        },
        {
            "id": 3,
            "input_type": "float",
            "value": 4.5
        }
    ]
    return samples
async def main():
    tasks = []
    for sample in get_user_input():
        input_value = sample["value"]
        if isinstance(input_value, str):
            task = asyncio.create_task(process_branch_a(input_value))
        elif isinstance(input_value, int):
            task = asyncio.create_task(process_branch_b(int(input_value)))
        else:
            task = asyncio.create_task(process_branch_c(float(input_value)))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)
if __name__ == '__main__':
    asyncio.run(main())