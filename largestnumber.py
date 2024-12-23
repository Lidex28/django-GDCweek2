def find_largest_number(numbers):
    if not numbers:
        return None 
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
numbers = [5, 12, 45, 7, 22]
print("Largest number:", find_largest_number(numbers))
