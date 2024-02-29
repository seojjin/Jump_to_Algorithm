# P1, P2, P3를 순서대로 이은 선분이 반시계 방향을 나타내면 1, 시계 방향이면 -1, 일직선이면 0
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

ccw = (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1) # 벡터의 외적 활용

if ccw > 0 :
    print(1)
elif ccw < 0:
    print(-1)
else:
    print(0)
