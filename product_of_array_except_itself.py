def product_except_self(nums):
    n = len(nums)
    
    # Initialize arrays
    left_products = [1] * n
    right_products = [1] * n
    
    # Calculate products to the left
    left_product = 1
    for i in range(1, n):
        left_product *= nums[i - 1]
        left_products[i] = left_product
    
    # Calculate products to the right
    right_product = 1
    for i in range(n - 2, -1, -1):
        right_product *= nums[i + 1]
        right_products[i] = right_product
    
    # Calculate final result
    result = [left_products[i] * right_products[i] for i in range(n)]
    
    return result

# Example usage:
nums = [1, 2, 3, 4]
result = product_except_self(nums)
print(result)  # Output: [24, 12, 8, 6]
