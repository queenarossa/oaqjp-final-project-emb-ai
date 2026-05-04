def emotion_detector(text_to_analyze):
    # Karena API IBM memblokir koneksi dari luar Lab, 
    # kita buat jawaban simulasi agar server.py milikmu bisa jalan di VS Code.
    
    if not text_to_analyze:
        return {
            'anger': None, 'disgust': None, 'fear': None, 
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }
    
    # Jawaban pura-pura (Simulasi) agar aplikasi webmu muncul di localhost:5000
    return {
        'anger': 0.1,
        'disgust': 0.05,
        'fear': 0.05,
        'joy': 0.7,
        'sadness': 0.1,
        'dominant_emotion': 'joy'
    }