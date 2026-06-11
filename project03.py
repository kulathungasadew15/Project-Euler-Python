def find_largest_prime_factor(n):
    factor = 2
    
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return n

target_number = 600851475143
result = find_largest_prime_factor(target_number)

print(f"The largest prime factor of {target_number} is: {result}")
