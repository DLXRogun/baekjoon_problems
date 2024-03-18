'''
1. 입력을 총 28줄로 주어진다.
2. 출력은 2줄로 1번째줄엔 안한 놈중 가장 적은 출석번호 
3. 어떤 알고리즘으로 접근해야될까
4. 일단 범위를 1~30 , 고정에 중복없이면 튜플이나 집합 괜찮겠네
5. 그리고 안쓴놈은 어떻게 찾지 if? while?
6. 입력 받은 놈들을 저장하고 전체 집합에서 지우고
7. 거기서 최소와 최대를 출력하면 되겠다.
'''
# 1~30번 까지 학생들 
all_student = [i for i in range(1,31)]
# print(all_student)

# good student 저장할 공간
good_student = 0

# 과제를 제출한 학생들 입력 받기
for n in range(1,29):
    good_student = int(input())
    all_student.remove(good_student)

print(min(all_student))
print(max(all_student))

