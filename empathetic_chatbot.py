import re
import random

class EmpatheticChatbot:
    def __init__(self):
        # Define keywords for each emotion scenario
        self.emotion_keywords = {
            'sad': ['sad', 'depressed', 'unhappy', 'down', 'miserable', 'heartbroken', 'lonely', 'crying', 'tears', 'grief', 'sorrow'],
            'happy': ['happy', 'joy', 'excited', 'great', 'wonderful', 'amazing', 'fantastic', 'awesome', 'delighted', 'pleased', 'ecstatic'],
            'stressed': ['stressed', 'anxious', 'overwhelmed', 'pressure', 'tense', 'worried', 'nervous', 'panic', 'burnout', 'exhausted']
        }
        
        # Empathetic responses for each emotion
        self.responses = {
            'sad': [
                "I'm really sorry you're feeling this way. That sounds really tough.",
                "It's okay to feel sad sometimes. Your feelings are valid.",
                "I hear you, and I'm here for you. Would you like to talk about what's bothering you?",
                "That sounds really difficult. I'm sending you virtual support."
            ],
            'happy': [
                "That's wonderful to hear! I'm so happy for you!",
                "Your joy is contagious! Tell me more about what made you feel this way.",
                "That's fantastic! Celebrating your happiness with you!",
                "I love hearing about your positive experiences! What else made your day great?"
            ],
            'stressed': [
                "I understand that stress can be overwhelming. Would it help to take a few deep breaths?",
                "It sounds like you're under a lot of pressure. Remember to be kind to yourself.",
                "Stress can be really tough to handle. Have you tried taking a short break to reset?",
                "I'm here for you. Sometimes just talking about what's stressing you can help lighten the load."
            ]
        }
        
        # Supportive suggestions for each emotion
        self.suggestions = {
            'sad': [
                "Would you like to try a short mindfulness exercise? It might help you feel a bit better.",
                "Sometimes writing down your feelings can help process them. Would you like to try that?",
                "Connecting with a friend or loved one might help. Is there someone you could reach out to?",
                "Taking a walk in nature can sometimes lift your mood. Would that be possible for you today?"
            ],
            'happy': [
                "Why not celebrate this moment? Do something special to mark this happy time!",
                "Sharing your happiness with others can multiply the joy. Who could you tell about this?",
                "Take a moment to really savor this feeling. What specifically made this so wonderful?",
                "This positive energy is great! How can you carry this feeling forward into the rest of your day?"
            ],
            'stressed': [
                "Try the 4-7-8 breathing technique: inhale for 4 seconds, hold for 7, exhale for 8. It can help calm your nervous system.",
                "Breaking your tasks into smaller steps might make them feel more manageable. Want to try that together?",
                "Setting boundaries is important when you're feeling overwhelmed. Is there something you can say 'no' to right now?",
                "A short 10-minute break to stretch or walk around might help reset your mind. Can you take that time for yourself?"
            ]
        }
        
        # Default responses when no emotion is detected
        self.default_responses = [
            "I'm here to listen. How are you feeling today?",
            "I care about how you're doing. Would you like to share what's on your mind?",
            "Your feelings matter to me. Is there something specific you'd like to talk about?",
            "I'm all ears. What's going on in your world right now?"
        ]
    
    def detect_emotion(self, user_input):
        """Detect the primary emotion in the user's message"""
        user_input = user_input.lower()
        
        # Count matches for each emotion
        emotion_scores = {'sad': 0, 'happy': 0, 'stressed': 0}
        
        for emotion, keywords in self.emotion_keywords.items():
            for keyword in keywords:
                if re.search(r'\b' + keyword + r'\b', user_input):
                    emotion_scores[emotion] += 1
        
        # Return the emotion with the highest score, or None if no emotion detected
        max_emotion = max(emotion_scores, key=emotion_scores.get)
        return max_emotion if emotion_scores[max_emotion] > 0 else None
    
    def generate_response(self, user_input):
        """Generate an empathetic response based on detected emotion"""
        emotion = self.detect_emotion(user_input)
        
        if emotion:
            # Select a random response and suggestion for the detected emotion
            response = random.choice(self.responses[emotion])
            suggestion = random.choice(self.suggestions[emotion])
            return f"{response}\n{suggestion}"
        else:
            # Use a default response if no emotion is detected
            return random.choice(self.default_responses)
    
    def start_chat(self):
        """Start the chatbot conversation"""
        print("Hello! I'm your empathetic chatbot. I'm here to listen and support you.")
        print("You can talk to me about how you're feeling. Type 'quit' to end our conversation.\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Chatbot: Thank you for talking with me. Take care of yourself!")
                break
            
            if not user_input:
                print("Chatbot: I'm here whenever you're ready to talk.")
                continue
            
            response = self.generate_response(user_input)
            print(f"Chatbot: {response}\n")

# Run the chatbot
if __name__ == "__main__":
    bot = EmpatheticChatbot()
    bot.start_chat()