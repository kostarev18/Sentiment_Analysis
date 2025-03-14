from django.shortcuts import render
from django.http import JsonResponse
from textblob import TextBlob
from .models import Submission
# Create your views here.

def sentiment_analysis(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    return "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"

def analyze_view(request):
    if request.method == "POST":
        text = request.POST['text']
        sentiment = sentiment_analysis(text)
        Submission.objects.create(text=text, sentiment=sentiment)
        return JsonResponse({"sentiment":sentiment})
    
    return render(request,"analysis/analyze.html")