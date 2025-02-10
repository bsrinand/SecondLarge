def second_largest(arr):
    unique_arr = list(set(arr))
    unique_arr.sort()
    return unique_arr[-2] if len(unique_arr) > 1 else None

arr = [10, 5, 8, 12, 12, 7]
print(second_largest(arr))  # Output: 10
