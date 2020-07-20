data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print('留言的平均長度為', sum_len/len(data))


new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言提到good')

#文字計數
wc = {} # word_count
for d in data:
    words= d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 # 新增新的KEY進WC字典

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print(len(wc))
print(wc['James'])

while True:
    word = input('請問你想查什麼字:')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為: ', wc[word])
    else:
        print('這個字還沒有出現過喔')

print('感謝使用本查詢系統')    
    


















# sum_len = 0
# for d in data:
# 	sum_len += len(d)

# print('留言的平均長度是', sum_len/len(data))


# new = []
# for d in data:
# 	if len(d) < 100:
		# new.append(d)
# print('一共有', len(new), '筆資料長度小於100')
# print(new[0])


# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)

# good = [d for d in data if 'good' in d] 等同上面4句的速寫法
# print('一共有', len(good), '筆留言提到good')
# print(good[0])