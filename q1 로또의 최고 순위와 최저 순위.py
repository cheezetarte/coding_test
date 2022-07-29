# 로또의 최고 순위와 최저 순위

def scores(x):
    return 6-max(x,1)+1

def solution(lottos, win_nums):
    i = 0
    
    for x in lottos:
        if x in win_nums:
            i += 1
            
    return [scores(i+lottos.count(0)), scores(i)]
