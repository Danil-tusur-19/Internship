import cv2

# Подключаемся к камере
cap = cv2.VideoCapture(0)

# Создаем объект для вычитания фона
fgbg = cv2.createBackgroundSubtractorMOG2()


while cap.isOpened():
        # Захват кадр за кадром
          ret, frame = cap.read()
          if ret:
            # Вычитание фона
            fg_mask = fgbg.apply(frame)

            # Поиск контура
            contours, hierarchy = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            min_contour_area = 800
            large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]
            # показать итоговый кадр

            frame_out = frame.copy()
            for cnt in large_contours:
                x, y, w, h = cv2.boundingRect(cnt)
                frame_out = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 200), 3)

            # отображаем результат
            cv2.imshow('Frame_final', frame_out)

            # Выход по нажатию 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cap.release()
cv2.destroyAllWindows()

wdwdafafafaw
fawawfawawfawfawfawfawf
afawf