# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

numbers = [1, 3, 2, 3, 4, 1, 3, -1, 5, 5, 4, 4]

def most_frequent(numbers):
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    print(max(frequency, key=frequency.get))

most_frequent(numbers)

"""
Time and Space Analysis for problem 1:
- Best-case: Only 1 element is present
- Worst-case: Multiple or no elements are most frequent
- Average-case: Finds 1 most frequent element
- Space complexity: O(n)
- Why this approach? It needs to check the whole list to determine the most frequent element.
- Could it be optimized? Not really, since all elements need to be checked.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

nums = [4, 5, 4, 6, 5, 7, 8, 9, 9, -1, 3]

def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    print(result)

remove_duplicates(nums)

"""
Time and Space Analysis for problem 2:
- Best-case: No duplicates are present
- Worst-case: All elements are duplicates
- Average-case: Some duplicates are present
- Space complexity: O(n)
- Why this approach? It uses a set to track seen elements and a list to preserve order.
- Could it be optimized? Not really, since all elements need to be checked.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

nums = [1, 2, 3, 4, 5, 0, 6, -1, -2]
target = 5

def find_pairs(nums, target):
    seen = set()
    pairs = []
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    print(pairs)


find_pairs(nums, target)

"""
Time and Space Analysis for problem 3:
- Best-case: No pairs sum to the target
- Worst-case: All pairs sum to the target
- Average-case: Some pairs sum to the target
- Space complexity: O(n)
- Why this approach? It uses a set to track seen elements and finds pairs efficiently.
- Could it be optimized? Not really, since all elements need to be checked.

Old solution - O(n^2) due to comparing each element with every other element for solutions.
Performance optimized - O(n) due to using a set to track seen elements and finding pairs efficiently.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

n = [1, 6, 12, 14, 23, 29, 32]

def add_n_items(n):
    capacity = 4
    lst = [0] * capacity
    for i in range(n):
        if i >= capacity:
            print(f"Resizing from {capacity} to {capacity * 2}")
            new_lst = [0] * (capacity * 2)
            for j in range(capacity):
                new_lst[j] = lst[j]
            lst = new_lst
            capacity *= 2
        lst[i] = i + 1

add_n_items(n)

"""
Time and Space Analysis for problem 4:
- When do resizes happen? When the list reaches its current capacity.
- What is the worst-case for a single append? O(n), where n is the current capacity.
- What is the amortized time per append overall? O(1)
- Space complexity: O(n)
- Why does doubling reduce the cost overall? Doubling reduces the frequency of resizes, making the average cost per append constant.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

nums = [1, 2, 3, 4, 10, 5, -9]

def running_total(nums):
    result = []
    total = 0
    for num in nums:
        total += num
        result.append(total)
    print(result)

running_total(nums)

"""
Time and Space Analysis for problem 5:
- Best-case: All elements are positive and the list is short
- Worst-case: The list contains many negative numbers and is long
- Average-case: The list contains a mix of positive and negative numbers
- Space complexity: O(n)
- Why this approach? It uses a single pass to compute the running total efficiently.
- Could it be optimized? Not really, since each element must be added to the total.
"""
