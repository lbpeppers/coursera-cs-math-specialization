def fn():
  n = 1000
  count = 0
  for i in range(n):
    for j in range(n):
      for k in range(n):
        if i < j and j < k:
          count = count + 1
  return count


print(fn())