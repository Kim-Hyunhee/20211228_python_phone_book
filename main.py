# 다른 모듈에 -> 메뉴 출력, 전화번호 추가 등등의 기능을 함수로 만들자
# 해당 함수들을 import해서 사용하자 
from phone_book import print_menu, add_phone_num, show_all_phone_num  # 하나의 py 파일에서 여러 함수 동시에 import

from time import sleep

# 메뉴에 0번을 입력할 때까지 계속해서 입력을 받고싶다.
# 무한 반복 => 0번이 들어오면 반복 종료

while True:
    # 실행 결과로 -> 어떤 숫자를 넣었는가? 받을 수 있다.
    num = print_menu()

    # num에 어떤 숫자가 담겼는가? 다른 행동(기능) 수행
    # 0번 : 프로그램 종료 => 우선 작업
    if num == 0:
        print('프로그램을 종료합니다.')
        break  # 무한 반복 탈출 => 프로그램 종료
    elif num == 1:
        # 전화번호부 기능 -> 전화번호 데이터 추가 기록
        add_phone_num()
    elif num == 2:
        # 전화번호부 기능 -> 모든 목록 표시
        show_all_phone_num()
    else :
        # 잘못된 숫자 들어옴. 안내 메시지만
        print('잘못된 입력입니다. 다시 입력해주세요.') # 참고 - 이 문장이 출력되고 나서 2초정도 대기(!) => 다음 문장 실행
        sleep(2)  # time 모듈의 sleep 기능 활용
        