<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Breathing Exercises</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f4f4f4;
            margin: 20px;
        }
        .container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 500px;
            margin: auto;
        }
        .circle {
            width: 100px;
            height: 100px;
            background-color: #007BFF;
            border-radius: 50%;
            margin: 20px auto;
        }
        button {
            padding: 10px;
            border: none;
            background-color: #28a745;
            color: white;
            cursor: pointer;
            border-radius: 5px;
            margin: 5px;
        }
        button:hover {
            background-color: #218838;
        }
        select {
            padding: 5px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Breathing Exercises</h2>
        <p>Select an exercise and follow the animation.</p>
        <select id="exerciseType">
            <option value="relax">Relaxation Breathing</option>
            <option value="energize">Energizing Breathing</option>
            <option value="focus">Focus Breathing</option>
        </select>
        <div class="circle" id="breathingCircle"></div>
        <button onclick="startBreathing()">Start Exercise</button>
    </div>

    <script>
        function startBreathing() {
            let circle = document.getElementById("breathingCircle");
            let exerciseType = document.getElementById("exerciseType").value;
            let duration = 4000;
            
            if (exerciseType === "relax") {
                duration = 5000;
            } else if (exerciseType === "energize") {
                duration = 3000;
            } else if (exerciseType === "focus") {
                duration = 4000;
            }
            
            circle.style.transition = `transform ${duration / 1000}s ease-in-out`;
            
            function breathe() {
                circle.style.transform = "scale(1.5)";
                setTimeout(() => {
                    circle.style.transform = "scale(1)";
                }, duration);
            }
            
            breathe();
            setInterval(breathe, duration * 2);
        }
    </script>
</body>
</html>
